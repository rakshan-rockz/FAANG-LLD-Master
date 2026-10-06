#!/usr/bin/env bash
# Compile and run the learner's C++ or Java code with warnings and runtime checks.
#
# Usage:
#   tools/run.sh <file.cpp | dir> [args...]          build + run the demo/driver (dir: all .cpp except tests)
#   tools/run.sh --test <dir | tests.cpp> [args...]  build + run the tests (dir: all .cpp except main.cpp)
#   tools/run.sh <File.java | dir-with-java> [args]  javac + java -ea (entry class Main; --test → Tests)
# Env:
#   TSAN=1     use -fsanitize=thread instead of ASan/UBSan (only if it links on this machine)
#   NOCHECK=1  plain -O2 build (timing / benchmarks)
#   INPUT=f    feed file f on stdin
# C++ flags: -std=c++20 -Wall -Wextra -Wshadow -pthread + checks (see tools/_flags.sh)
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"; source "$root/tools/_flags.sh"
mode=run; if [ "${1:-}" = "--test" ]; then mode=test; shift; fi
src="${1:?usage: tools/run.sh [--test] <file|dir> [args...]}"; shift || true
build="$root/designs/.build"; mkdir -p "$build"
name="$(basename "${src%.*}")"; [ "$mode" = test ] && name="$name.test"

# ---- Java --------------------------------------------------------------------------------------
if [[ "$src" == *.java ]] || { [ -d "$src" ] && [ -n "$(find "$src" -name '*.java' -print -quit)" ] && [ -z "$(find "$src" -name '*.cpp' -print -quit)" ]; }; then
  out="$build/java-$name"; rm -rf "$out"; mkdir -p "$out"
  if [ -d "$src" ]; then mapfile -t files < <(find "$src" -name '*.java' | sort); else files=("$src"); fi
  javac -Xlint:all -d "$out" "${files[@]}"
  entry="Main"; [ "$mode" = test ] && entry="Tests"
  cls=$(cd "$out" && find . -name "$entry.class" | head -1 | sed 's|^\./||; s|\.class$||; s|/|.|g')
  [ -n "$cls" ] || { echo "no $entry class found in $src" >&2; exit 2; }
  exec java -ea -cp "$out" "$cls" "$@"
fi

# ---- C++ ---------------------------------------------------------------------------------------
mapfile -t files < <(cpp_sources "$src" "$mode")
[ ${#files[@]} -gt 0 ] || { echo "no .cpp sources found in $src (mode $mode)" >&2; exit 2; }
if [ "${NOCHECK:-0}" = "1" ]; then chk="-O2"
elif [ "${TSAN:-0}" = "1" ]; then chk="-O1 -g $(check_flags "$build" thread)"
else chk="-O1 -g $(check_flags "$build")"; fi
inc=""; [ -d "$src" ] && inc="-I$src"
bin="$build/$name"
# shellcheck disable=SC2086
g++ -std=c++20 -Wall -Wextra -Wshadow -pthread $chk $inc -I"$root/designs/lib" "${files[@]}" -o "$bin"
start=$(date +%s%N); set +e
if [ -n "${INPUT:-}" ]; then "$bin" "$@" < "$INPUT"; else "$bin" "$@"; fi
rc=$?; end=$(date +%s%N)
echo "[exit $rc · $(( (end - start) / 1000000 )) ms]" >&2
exit $rc
