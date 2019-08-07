import React from 'react';
import axios from 'axios';


const API_KEY = "5f2b00a991eef055a54a22efc396872d"
//"api.themoviedb.org/3/search/movie?api_key={API_KEY}&query=inception&page=1"
const useTmdb = movie => {
    const [data, setData] = React.useState({});
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState(false);


    React.useEffect(() => {
        const getData = async date =>{
            try{
                setError(false);
                setLoading(true);
                const response = await axios.get(
                    `https://api.themoviedb.org/3/search/movie?api_key=${API_KEY}&query=${movie}&page=1`,
                );
                setData(response.data);
                // console.log("Testing")
                // console.log(response)
                // console.log("Data:")
                // console.log(data)
                setLoading(false);
            }catch(error){
                console.log(error);
                setLoading(false);
                setError(true);
            }
        };
        getData(movie);
    }, [movie]);
    
    
    return {
        data,
        loading,
        error,
    };
}

export default useTmdb