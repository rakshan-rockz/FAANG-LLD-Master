#!/usr/bin/env bash
# Concurrency stress runner: build once, run the program many times to surface rare interleavings,
# lost updates, assertion failures and deadlocks (a run exceeding the timeout is reported as a hang).
#
# Usage: tools/stress.sh [--test] <file.cpp | dir> [runs=200] [timeout-seconds=10] [-- program args...]
#   --test      build the tests (dir: all .cpp except main.cpp) instead of the driver
# Env: TSAN=1 (default here) tries -fsanitize=thread; TSAN=0 uses ASan/UBSan probes instead.
#      JITTER=1 (default) runs some iterations under `taskset -c 0` (1 core → different schedules)
# The program must exit non-zero (e.g. assert / abort) when its own invariant check fails.
set -uo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"; source "$root/tools/_flags.sh"
mode=run; if [ "${1:-}" = "--test" ]; then mode=test; shift; fi
src="${1:?usage: tools/stress.sh [--test] <file|dir> [runs] [timeout] [-- args]}"; shift
runs="${1:-200}"; [ $# -gt 0 ] && shift; tmo="${1:-10}"; [ $# -gt 0 ] && shift
[ "${1:-}" = "--" ] && shift
build="$root/designs/.build"; mkdir -p "$build"
mapfile -t files < <(cpp_sources "$src" "$mode")
[ ${#files[@]} -gt 0 ] || { echo "no .cpp sources found in $src" >&2; exit 2; }
if [ "${TSAN:-1}" = "1" ]; then chk="$(check_flags "$build" thread)"; else chk="$(check_flags "$build")"; fi
inc=""; [ -d "$src" ] && inc="-I$src"
bin="$build/stress_$(basename "${src%.*}")"
# shellcheck disable=SC2086
g++ -std=c++20 -O1 -g -Wall -Wextra -pthread $chk $inc -I"$root/designs/lib" "${files[@]}" -o "$bin" || exit 2
pin=""; command -v taskset >/dev/null && pin="taskset -c 0"
fails=0; hangs=0
for ((i = 1; i <= runs; i++)); do
  runner=""; if [ "${JITTER:-1}" = "1" ] && [ -n "$pin" ] && (( i % 4 == 0 )); then runner="$pin"; fi
  # shellcheck disable=SC2086
  timeout "$tmo" $runner "$bin" "$@" > "$build/stress_out.txt" 2> "$build/stress_err.txt"; rc=$?
  if [ $rc -eq 124 ]; then
    hangs=$((hangs + 1)); echo "✗ run $i: HANG (> ${tmo}s): deadlock, lost wakeup or livelock?${runner:+ [1 core]}"
  elif [ $rc -ne 0 ]; then
    fails=$((fails + 1)); echo "✗ run $i: exit $rc${runner:+ [1 core]}"; head -8 "$build/stress_err.txt"; tail -3 "$build/stress_out.txt"
  fi
  if (( fails + hangs >= 3 )); then echo "Stopping after 3 failures. Reproduce, then reason about the interleaving by hand."; exit 1; fi
done
if (( fails + hangs == 0 )); then echo "✓ $runs runs clean (no failures, no hangs). Clean runs are evidence, not proof: argue the invariant."
else echo "✗ $fails failures, $hangs hangs in $runs runs"; exit 1; fi
