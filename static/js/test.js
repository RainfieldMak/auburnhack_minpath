//https://www.codexworld.com/add-remove-input-fields-dynamically-using-jquery/


$(document).ready(function(){

    /* limit input waypoint to be <=10 */
    var max_way_point= 10; 
    var addButton = $ (".add_field_btn");
    var wrapper = $(".field_wrapper");

    /*new way point field */
    var fieldHTML="<div> <label for='start'>Way point</label><input type='text' id='start' name='field_name[]' value=''/><a href='javascript:void(0);' class='remove_btn'> remove</a> </div>"






    /*initial start waypoint   0th base */
    var waypoint_count=1;

    


    /* on click add button */
    $(addButton).click(function()
    {
        if( waypoint_count< 10)
        {
            waypoint_count++;
            $(wrapper).append(fieldHTML);
        }
    
    
    });


    /*remove button */
    $(wrapper).on("click", '.remove_btn',function(e)
    {
        /*remove btn is a <a> , preventDefault prevent it going to antoehr link*/
        e.preventDefault();

        /* remove the field html*/
        $(this).parent('div').remove();

        waypoint_count--;
    }
   
    );




    /*submit button for getting value from textfield */
    $("#sub_btn1").click(function(){

        /* sanity check */
       alert("Submit ?");

        /*get all input text field (start, destinations, waypoint 1... waypoint n) */
        /*https://stackoverflow.com/questions/24503865/how-to-get-all-the-values-of-input-array-element-jquery*/
       var search_string_list= $("input[name='field_name[]']").map(
                                                                    function()
                                                                        {return $(this).val();}
                                                                    ).get();

        const content = JSON.stringify({"name":search_string_list})
        console.log(content);

        
        
        /*
        var a = document.createElement("a");
        var file = new Blob([content], {type: 'text/plain'});
        a.href = URL.createObjectURL(file);
        a.download = "raw_input.txt";
        a.click();
        */
        var url= "/receive_input";
        console.log(content);

        var csrf_token = "{{ csrf_token() }}";
        

        $.ajax
        (
            {
                method:'POST',
                url:'/submit',
                data:content,
                contentType: "application/json",
                
                success: function(){
                    console.log("check terminal \n");
                },
                erro:function(){
                    consolge.log("Fail");
                },

            }

        );




     });




 });