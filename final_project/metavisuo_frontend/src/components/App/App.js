import React from 'react';
import {Route} from 'react-router-dom';

import homePage from '../HomePage/HomePage';
import "bootstrap/dist/css/bootstrap.min.css";
import "shards-ui/dist/css/shards.min.css"

const App=()=>{
    return (
        <div>
            
            <Route path="/movies/" exact component={homePage}/>
        </div>
    );
}

export default App;