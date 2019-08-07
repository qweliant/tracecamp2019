import React, {useState, useContext} from "react";


const ExampleContext = React.createContext();

//use context to store variable 
function ExampleProvider(props){
    const [num, setNum] = useState(7);
    const addObj = {number: num, addOne: () => setNum(num+1)};
    return( 
        <ExampleContext.Provider value={addObj} >
            {props.children}
        </ExampleContext.Provider>
    );
}


function One(props){
    const mynum = useContext(ExampleContext);
    return (
        <div>
            <h1>
                {mynum.number}
                <button onClick={mynum.addOne}>Add One</button>
            </h1>
        </div>
    );
}

function Two(props){
    return(
        <div>            
            <One/>
        </div>
    );
}

function Pass(){
    
    return( 
        <div>
            <h1> YOUUU SHALLL NOTTT PASSSSSSSSSSS THIS CONTEXT API EXAMPLE </h1>
            <ExampleProvider>
                <Two/>
            </ExampleProvider>
        </div>
    )
}

export default Pass;