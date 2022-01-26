

PARRENT_COMMIT=`git rev-list --all --parents --max-count=1`
IFS=' ' read -ra COMMIT <<< "$PARRENT_COMMIT"
VAR=`git diff --name-only HEAD ${COMMIT[1]}`
DIR="$(dirname "${VAR}")" ; FILE="$(basename "${VAR}")"
if [ "$DIR" != "." ]; then
  cd $DIR
  dockerfile=`ls Dockerfile.*`
  IFS='.' read -ra names_array <<< "$dockerfile"
  echo Building ${names_array[1]}/${names_array[2]}
  if [ $1 = "build" ]; then
   docker build . --file $dockerfile --tag ${names_array[1]}/${names_array[2]}
  fi
  if [ $1 = "push" ]; then
   docker push ${names_array[1]}/${names_array[2]}
  fi
fi



    
# counter=0
# for file in ./*/
# do
#   if [ $counter -ge 1 ]; then
#     cd ../
#   fi
#   cd $file
#   wd=`pwd`
#   dockerfile=`ls Dockerfile.*`
#   IFS='.' read -ra names_array <<< "$dockerfile"
#     echo Building ${names_array[1]}/${names_array[2]}
#     if [ $1 = "build" ]; then
#       docker build . --file $dockerfile --tag ${names_array[1]}/${names_array[2]}
#     fi
#     if [ $1 = "push" ]; then
#       docker push ${names_array[1]}/${names_array[2]}
#     fi
#   ((counter++))
# done
