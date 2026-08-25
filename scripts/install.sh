#!/usr/bin/env bash
# Install the skills in this repository into an agent's skills directory.
#
# Every host reads the same SKILL.md folder; only the location differs. This
# script symlinks (or copies) the skill into the right place for the hosts
# below. For anything else, use `npx skills add opuu/bangla-writer`, which knows
# the paths for 76+ agents, or pass --dir with an explicit target.
#
#   ./scripts/install.sh claude              # user scope, symlink
#   ./scripts/install.sh codex --scope project
#   ./scripts/install.sh copilot --copy
#   ./scripts/install.sh --dir ~/somewhere/skills
#   ./scripts/install.sh --list

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO/skills"
SCOPE=user
MODE=symlink
TARGET=""
HOST=""

user_dir() {
  case "$1" in
    claude)       echo "$HOME/.claude/skills" ;;
    codex)        echo "$HOME/.agents/skills" ;;
    antigravity)  echo "$HOME/.agents/skills" ;;
    antigravity1) echo "$HOME/.gemini/config/skills" ;;
    gemini)       echo "$HOME/.gemini/skills" ;;
    cursor)       echo "$HOME/.cursor/skills" ;;
    copilot)      echo "$HOME/.copilot/skills" ;;
    opencode)     echo "$HOME/.config/opencode/skills" ;;
    agents)       echo "$HOME/.agents/skills" ;;
    *)            echo "" ;;
  esac
}

project_dir() {
  case "$1" in
    claude)       echo ".claude/skills" ;;
    codex)        echo ".agents/skills" ;;
    antigravity)  echo ".agents/skills" ;;
    antigravity1) echo ".gemini/skills" ;;
    gemini)       echo ".gemini/skills" ;;
    cursor)       echo ".cursor/skills" ;;
    copilot)      echo ".github/skills" ;;
    opencode)     echo ".opencode/skills" ;;
    agents)       echo ".agents/skills" ;;
    *)            echo "" ;;
  esac
}

HOSTS="claude codex antigravity antigravity1 gemini cursor copilot opencode agents"

usage() {
  cat <<EOF
usage: install.sh [host] [--scope user|project] [--copy] [--dir PATH] [--list]

hosts:
  claude        Claude Code                ~/.claude/skills      .claude/skills
  codex         OpenAI Codex               ~/.agents/skills      .agents/skills
  antigravity   Antigravity 2.0 / CLI      ~/.agents/skills      .agents/skills
  antigravity1  Antigravity (older)        ~/.gemini/config/skills
  gemini        Gemini CLI                 ~/.gemini/skills      .gemini/skills
  cursor        Cursor                     ~/.cursor/skills      .cursor/skills
  copilot       GitHub Copilot             ~/.copilot/skills     .github/skills
  opencode      OpenCode                   ~/.config/opencode/skills
  agents        neutral location           ~/.agents/skills      .agents/skills

options:
  --scope user|project   install for the current user (default) or into ./
  --copy                 copy files instead of symlinking
  --dir PATH             install into PATH, ignoring the host table
  --list                 print resolved paths and exit
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --scope) SCOPE="${2:?--scope needs a value}"; shift 2 ;;
    --copy) MODE=copy; shift ;;
    --dir) TARGET="${2:?--dir needs a path}"; shift 2 ;;
    --list)
      printf '%-14s %-32s %s\n' HOST USER PROJECT
      for h in $HOSTS; do printf '%-14s %-32s %s\n' "$h" "$(user_dir "$h")" "$(project_dir "$h")"; done
      exit 0 ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "unknown option: $1" >&2; usage >&2; exit 2 ;;
    *) HOST="$1"; shift ;;
  esac
done

if [ -z "$TARGET" ]; then
  [ -n "$HOST" ] || { usage >&2; exit 2; }
  case "$SCOPE" in
    user)    TARGET="$(user_dir "$HOST")" ;;
    project) TARGET="$(project_dir "$HOST")" ;;
    *) echo "--scope must be 'user' or 'project'" >&2; exit 2 ;;
  esac
  [ -n "$TARGET" ] || { echo "unknown host '$HOST' (try --list)" >&2; exit 2; }
fi

mkdir -p "$TARGET"
for skill in "$SRC"/*/; do
  [ -f "$skill/SKILL.md" ] || continue
  name="$(basename "$skill")"
  dest="$TARGET/$name"
  rm -rf "$dest"
  if [ "$MODE" = copy ]; then
    cp -R "$skill" "$dest"
  else
    ln -s "${skill%/}" "$dest"
  fi
  echo "installed $name -> $dest ($MODE)"
done
