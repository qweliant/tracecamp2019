import React, {useState} from 'react';


const MoviePicker = ({match, history}) =>{
    const movie = match.params.movie
    console.log(movie)
    const [input, setInput] = useState('');
   

    const handleChange=(event)=>{
        setInput(event.target.value);
    }

    const addItem=(event)=>{
        event.preventDefault();
        setInput("");
    }

    const inputHandler =(event)=>{
        const movie = event.target.value;
        console.log(movie);
        history.push(`/movies/${movie}`)
    }

    return(
        <div>
            <form onSubmit={addItem}>
                <input type = "text" onChange={handleChange} value={input}/>
                <button onClick={inputHandler} type = "submit" value={input}>submit</button>
            </form>
            <h1>{input}</h1>

        </div>

    );
}

export default MoviePicker;