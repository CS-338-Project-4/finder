import logo from './logo.svg';
//import './App.css';
import { useState } from 'react';
import "./index.css";
import Title from './Title';

function App() {
  return (
    
  <div class="form-container">
    
      <form class="register-form">

      <Title />
        
        <input
          id="question"
          class="form-field"
          type="text"
          placeholder="Question"
          name="question"
        />
        
        <button class="form-field" type="submit">
          Option - 1
        </button>

        <button class="form-field" type="submit">
          Option - 2 
        </button>

        <button class="form-field" type="submit">
          Option - 3
        </button>

        <button class="form-field" type="submit">
          Option - 4
        </button>



      </form>
    </div>
  );
}

export default App;
