function displaypage(){
    var title = document.getElementById("title-input");
    var category = document.getElementById("category");
    var content = document.getElementById("content");
    var author = document.getElementById("author");
    if(title.value.length < 1){
        title.style.borderColor = "red";
        document.getElementsByClassName("error-message-title")[0].style.display = "block";

        category.style.borderColor = "unset";
        document.getElementsByClassName("error-message-category")[0].style.display = "none";

        content.style.borderColor = "unset";
        document.getElementsByClassName("error-message-content")[0].style.display = "none";

        author.style.borderColor = "unset";
        document.getElementsByClassName("error-message-author")[0].style.display = "none";
        return false;
    }

    else if(category.value == "select"){
        category.style.borderColor = "red";
        document.getElementsByClassName("error-message-category")[0].style.display = "block";

        title.style.borderColor = "unset";
        document.getElementsByClassName("error-message-title")[0].style.display = "none";

        content.style.borderColor = "unset";
        document.getElementsByClassName("error-message-content")[0].style.display = "none";

        author.style.borderColor = "unset";
        document.getElementsByClassName("error-message-author")[0].style.display = "none";
        return false;
    }
    else if(content.value.length < 50){
        title.style.borderColor = "unset";
        document.getElementsByClassName("error-message-title")[0].style.display = "none";

        category.style.borderColor = "unset";
        document.getElementsByClassName("error-message-category")[0].style.display = "none";

        content.style.borderColor = "red";
        document.getElementsByClassName("error-message-content")[0].style.display = "block";

        author.style.borderColor = "unset";
        document.getElementsByClassName("error-message-author")[0].style.display = "none";
        return false;
    }
    else if(author.value.length < 1){
        author.style.borderColor = "red";
        document.getElementsByClassName("error-message-author")[0].style.display = "block";

        category.style.borderColor = "unset";
        document.getElementsByClassName("error-message-category")[0].style.display = "none";

        title.style.borderColor = "unset";
        document.getElementsByClassName("error-message-title")[0].style.display = "none";

        content.style.borderColor = "unset";
        document.getElementsByClassName("error-message-content")[0].style.display = "none";
        return false;
    }
    else{
    window.location.replace("http://127.0.0.1:8000/posts");
    }
}

function new_post(){
    window.location.replace("http://127.0.0.1:8000");
}

function read_posts(){
    window.location.replace("http://127.0.0.1:8000/posts");
}