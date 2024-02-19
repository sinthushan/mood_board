const  imgs = document.querySelectorAll(".gallery-img");
const target = document.getElementById("canvas");
let dragged


imgs.forEach(img => img.addEventListener("dragstart", (event) => {
   
    dragged = event.target;
    event.dataTransfer.dropEffect = "copy";
    console.log("something is being dragged");
   
}));


imgs.forEach(img => img.addEventListener("dragend", (event) => {
   
    dragged = event.target;
    
    console.log("something is being dragged");
   
}));



target.addEventListener("dragover", (event) => { 
    event.preventDefault();
});

target.addEventListener("drop", (event) => {
    // prevent default action (open as link for some elements)
    event.preventDefault();
    
    event.target.appendChild(dragged);

});