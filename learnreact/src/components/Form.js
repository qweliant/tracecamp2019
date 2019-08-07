import React, {useState} from 'react';

function Form(){

    const [name, setName] = useState("John Wick");
    const [status, setStatus] = useState("");
    const [value, setValue] = useState("");

function handleChange(event){
    setValue(event.target.value)
    console.log(event)
}

function handleSubmit(event){
    event.preventDefault();
    setStatus(value);
    setValue("");
}

    return(
        <div>
            <h1>Form</h1>
            <h1>{name}</h1>
            <h1>{status}</h1>
            <form onSubmit={handleSubmit}>
                <input type = "text" placeholder="Add nameh" value={name}/>
                <input type = "text" placeholder="Change Status" value={value} onChange={handleChange}/>
                <input type = "submit"/>
            </form>
        </div>
    )
}

export default Form;