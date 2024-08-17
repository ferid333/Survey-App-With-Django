var sign = document.querySelector('.fa-plus') 
var mainform=document.querySelector(".mainform")
var options=document.querySelectorAll(".options")
var optioncount=1
sign.addEventListener("click",()=>{
    var submitbtn=document.querySelector(".submitbtn")
    if(optioncount>2){
        sign.style.opacity="0"
    }
    if(optioncount<4){
    // let div=document.createElement("div")
    // div.className="mb-3"
    // let label=document.createElement("label")
    // label.className="form-label"
    // label.textContent=`Option ${optioncount}`
    // let input=document.createElement("input")
    // input.className="form-control"
    // input.setAttribute("name",`option${optioncount}`)
    // input.setAttribute("required","required")
    let button=document.createElement("button")
    button.className="btn btn-primary submitbtn"
    button.setAttribute("type","submit")
    button.textContent="Submit"
    // div.appendChild(label)
    // div.appendChild(input)
    // mainform.appendChild(div)
    mainform.removeChild(submitbtn)
 
    // optioncount+=1
    for (let i = 0; i < optioncount; i++) {
        options[i].style.display="block"
        options[i].children[1].setAttribute("required","required")
    }
    mainform.appendChild(button)
    optioncount+=1
    }
})
