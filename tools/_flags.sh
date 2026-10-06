# Sourced by run.sh / stress.sh: picks the strongest checking flags this machine supports.
# Sanitizers need their runtime libraries (e.g. `sudo dnf install libasan libubsan libtsan`).
# Each sanitizer is used only if a probe program actually compiles AND links with it.
_probe() { echo 'int main(){}' > "$1/probe.cpp"; g++ -std=c++20 -pthread $2 "$1/probe.cpp" -o "$1/probe" 2>/dev/null; }

# check_flags <build-dir> [thread]
#   default : bounds-checked STL (always) + ASan/UBSan if they link
#   thread  : bounds-checked STL + TSan if it links (TSan cannot be combined with ASan)
check_flags() {
  local dir="$1" mode="${2:-}" f="-D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC"   # always available
  if [ "$mode" = "thread" ]; then
    if _probe "$dir" "-fsanitize=thread"; then f="$f -fsanitize=thread"
    else echo "[note] -fsanitize=thread does not link here (no libtsan): races are found by repetition only" >&2; fi
  else
    _probe "$dir" "-fsanitize=address" && f="$f -fsanitize=address -fno-omit-frame-pointer"
    _probe "$dir" "-fsanitize=undefined" && f="$f -fsanitize=undefined"
  fi
  echo "$f"
}

# cpp_sources <path> <mode>  → the .cpp files to compile.
#   file      → just that file
#   directory → every .cpp below it; mode=run excludes test*.cpp / *_test.cpp, mode=test excludes main.cpp
cpp_sources() {
  local p="$1" mode="$2"
  if [ -f "$p" ]; then echo "$p"; return; fi
  if [ "$mode" = "test" ]; then
    find "$p" -name '*.cpp' ! -name 'main.cpp' ! -path '*/.build/*' | sort
  else
    find "$p" -name '*.cpp' ! -name 'test*.cpp' ! -name '*_test.cpp' ! -name 'tests.cpp' ! -path '*/.build/*' | sort
  fi
}
