import logo from './logo.svg';
//import './App.css';
import { useState } from 'react';
import "./index.css";
import Title from './Title';

function App() {
  async function getPossibleNodes() {
    const apiUrl = 'https://www.wikidata.org/w/api.php?';
    let params = {
      action: 'wbsearchentities',
      search: 'python',  // TODO: get from state of question type input
      language: 'en',
      format: 'json',
      origin: '*'
    };
    let searchParams = new URLSearchParams(params);

    const response = await fetch(apiUrl + searchParams.toString());
    return response.json()
  };

  console.log(getPossibleNodes());

  return (

  <div className="form-container">

      <form className="register-form">

      <Title />

        <input
          id="question"
          className="form-field"
          type="text"
          placeholder="Question"
          name="question"
        />

        <button className="form-field" type="submit">
          Option - 1
        </button>

        <button className="form-field" type="submit">
          Option - 2
        </button>

        <button className="form-field" type="submit">
          Option - 3
        </button>

        <button className="form-field" type="submit">
          Option - 4
        </button>



      </form>
    </div>
  );
}

export default App;
