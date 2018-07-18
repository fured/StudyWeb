function setCookie(name,value,expiredays){
	var exdate = new Date;
    exdate.setDate(exdate.getDate()+expiredays)
	document.cookie = name+"="+escape(value)+((expiredays==null)?"":";expires="+exdate.toGMTString())
}
				 
function getCookie(name){
	if (document.cookie.length > 0){
		start=document.cookie.indexOf(name + "=")
		if (start!=-1){ 
			start=start + name.length+1 
			end=document.cookie.indexOf(";",start)
			if (end==-1) end=document.cookie.length 
				return unescape(document.cookie.substring(start,end))
		} 
		}
		return false
}

