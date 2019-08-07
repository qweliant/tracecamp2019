import axios from 'axios';
//import React from 'react';

//const API_KEY = "vHBKMUIfEIlk9zuU"




function getCurency(currency) {
    return axios.get(`https://api.coinbase.com/v2/exchange-rates?currency=${currency}`)
}

export default getCurency