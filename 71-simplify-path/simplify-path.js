/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    const arr = path.split("/")
    console.log(arr)

    let s=[]
    for(i=0;i<arr.length;i++)
    {
        if(arr[i]=='' || arr[i]=='.')
        continue
        else if(arr[i]=='..')
        s.pop();
        else
        s.push(arr[i])
    }
    let newstr =''
        while(s.length > 0)
        {
            newstr = s.pop() + '/' + newstr;
            // newstr += s.pop() + '/'
        }
        return '/'+newstr.substr(0,newstr.length -1);
}