import React from 'react';
import Movie from '../Movie/Movie';
import MoviePicker from '../MoviePicker/MoviePicker';
import Movies from '../Movies/Movies'
import {Route} from 'react-router-dom';

const App=()=>{
    return (
        <div>
            <Route path="/movies/" exact component={Movies} />
            <Route path="/movies/:movie" component={MoviePicker} />
            <Route path="/movies/:movie" component={Movie} />
        </div>
    );
}

export default App;