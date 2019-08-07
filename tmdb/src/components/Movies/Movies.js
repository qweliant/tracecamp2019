import React from 'react';


const Movies=({location, history})=>{
    const movie= "Inception"
    if(location.pathname === '/movies' || location.pathname === '/movies/'){
        history.replace(`/movies/${movie}`);
    }
    return <div>Movies</div>;

}


export default Movies;