VAR=`git diff --name-only HEAD HEAD~1`
DIR="$(dirname "${VAR}")" ; FILE="$(basename "${VAR}")"
cd $DIR

if [ "$DIR" != "/" ]; then
  dockerfile=`ls Dockerfile.*`
  IFS='.' read -ra names_array <<< "$dockerfile"
    echo Building ${names_array[1]}/${names_array[2]}
    if [ $1 = "build" ]; then
      docker build . --file $dockerfile --tag ${names_array[1]}/${names_array[2]}
    fi
    if [ $1 = "push" ]; then
      docker push ${names_array[1]}/${names_array[2]}
    fi
else

    
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
