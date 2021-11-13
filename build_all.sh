counter=0
for file in ./*/
do
  if [ $counter -ge 1 ]; then
    cd ../
  fi
  cd $file
  wd=`pwd`
  dockerfile=`ls Dockerfile.*`
  IFS='.' read -ra names_array <<< "$dockerfile"
    echo Building ${names_array[1]}/${names_array[2]}
    docker build . --file $dockerfile --tag ${names_array[1]}/${names_array[2]}
    docker push ${names_array[1]}/${names_array[2]}
  ((counter++))
done