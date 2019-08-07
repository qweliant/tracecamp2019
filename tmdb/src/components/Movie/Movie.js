import React from 'react';
import useTmdb from '../hooks/useTmdb/useTmdb';


//"api.themoviedb.org/3/search/movie?api_key={API_KEY}&query=inception&page=1"
const Movie = ({match}) =>{
    const movie = match.params.movie
    const { data, loading, error } = useTmdb(movie);
    
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error!</div>;
    
    console.log(data);
    console.log("Testing:")
    console.log(data["page"])
    console.log(data["results"])
    console.log(data["results"][0]["original_title"])
    
    return (
        <div >
            <h3>{data["results"][0]["original_title"]}</h3>
        </div>
    );
}

export default Movie