const solution = (my_string) => {
    [...'aeiou'].map(v=>{
        my_string = my_string.replaceAll(v,"")
    })
                     
    return my_string
}