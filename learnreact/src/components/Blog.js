import React, {useState} from "react";

function Blog(){
    const [list, setList] = useState([]);
    const [value, setValue] = useState("");

    function Number(props){
        function handleClick(){
            props.remove(props.id);
        }
        return (
            <div>{props.num}<button onClick={handleClick}>Delete</button></div>
        )
    }

    function handleChange(event){
        setValue(event.target.value);
    }

    function addItem(event){
        event.preventDefault();
        setList([...list, value]);
        setValue("");
    }

    function handleRemove(id){
        const newList = list.filter((item, index )=> index !== id);
        setList(newList);
    }



    return( 
        <div>
            
            {list.map((item, index) =>( <Number key={index}  num ={item} id={index} remove={handleRemove}/> ))}
            
            <form onSubmit={addItem}>
                <textarea type = "text" onChange={handleChange} value={value}/>
                    <input type = "submit" value="Submit"/>
            </form>

            <label for="post-select">Choose a post:</label>

            <select id="post-select">
                <option value="">Select Blog Post</option>


                {list.map((item, index) =>( <option key={index}  num ={item} id={index} remove={handleRemove}><button>{item}</button></option>))}


            </select>


        </div>
    );
}


export default Blog;




//"Had interesting talk with Bekk today about moraql relativism . 
//The limits of of which seem to echo reductionist "non-stance" 
//on issues, i.e. attempting to quantify the logic of math into one book. 
//The relativist might say, "one cannot define math, for the symbols used to 
//understand logic are relative to language". Insight: instead of 
//finding a single irreducible element to phrase "math", 
//one should open the framework of perception. Instead of making non-statements, one should seek meaning"