# Use `sam build` to get dependencies
sam build -b ./build --use-container -m ./requirements.txt

# Move dependencies into our layer directory
mv ./build/ServiceApiFunction/* ./src/
rm -rf ./build