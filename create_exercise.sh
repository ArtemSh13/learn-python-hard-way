#!/bin/bash
if [ "$1" = "file" ]; then
     touch "exercise_${2}.py"
fi
if [ "$1" = 'dir' ]; then
  mkdir "exercise_${2}"
  touch "exercise_${2}/exercise_${2}.py"
fi
exit 0