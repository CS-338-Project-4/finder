import logo from './logo.svg';
//import './App.css';
import { useState } from 'react';
import "./index.css";
import Title from './Title';

function App() {
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
