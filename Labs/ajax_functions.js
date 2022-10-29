function getAll(callback){
    $.ajax({
        "url": "http://andrewbeatty1.pythonanywhere.com/books",
        "method":"GET",
        "data":"",
        "dataType": "JSON",
        "success":function(result){
            callback(result)
 
        },
        "error":function(xhr,status,error){
            console.log("Error: "+status+" Msg: "+error);
        }
    });
}

function createBook(book, callback){
    console.log(JSON.stringify(book));
    $.ajax({
        "url": "http://andrewbeatty1.pythonanywhere.com/books",
        "method":"POST",
        "data":JSON.stringify(book),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success":function(result){
            
            callback(result)  
        },
        "error":function(xhr,status,error){
            console.log("Error: "+status+" Msg: "+error);
        }
    });
}
function updateBook(book, callback){
    
    $.ajax({
        "url": "http://andrewbeatty1.pythonanywhere.com/books/"+encodeURI(book.id),
        "method":"PUT",
        "data":JSON.stringify(book),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success":function(result){
            console.log(result);
            callback(result)   
        },
        "error":function(xhr,status,error){
            console.log("Error: "+status+" Msg: "+error);
        }
    });
}
function deleteBook(id, callback){
    $.ajax({
        "url": "http://andrewbeatty1.pythonanywhere.com/books/"+id,
        "method":"DELETE",
        "data":"",
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success":function(result){
            console.log(result);
            callback(result)  
        },
        "error":function(xhr,status,error){
            console.log("Error: "+status+" Msg: "+error);
        }
    });
}
