import axios from 'axios';

const API_KEY = "cGGh4pgW45NlrovpudcBvPVaLq8je7wp97M8yLID";

const getAsteroid = (start, end) => {
    return axios.get(`https://api.nasa.gov/neo/rest/v1/feed?start_date=${start}&end_date=${end}&api_key=${API_KEY} `)
}

export default getAsteroid;