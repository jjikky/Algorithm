const solution = (num_list)=>{
    let odd = num_list.filter(v=>v%2==1).length
    return [num_list.length-odd,odd]
}
