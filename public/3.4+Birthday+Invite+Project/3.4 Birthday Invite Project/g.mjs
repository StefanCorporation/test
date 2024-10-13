function* h(){
    yield 1
    yield 2
    yield 3
}

console.log(h().next())