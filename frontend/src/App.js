import logo from './logo.svg';
//import './App.css';
import { useState } from 'react';
import "./index.css";
import Title from './Title';
import Autocomplete from './Autocomplete';

function App() {
  async function getScores() {
    const apiUrl = 'http://localhost:8000/get-sparql?';
    let searchParams = new URLSearchParams();

    typeList.forEach(type => {
      searchParams.append('types', type);
    });

    answerList.forEach(answer => {
      searchParams.append('answers', answer);
    });

    const response = await fetch(apiUrl + searchParams.toString());
    return response.json()
  };

  const [typeList, setTypeList] = useState(['']);
  const [answerList, setAnswerList] = useState(['']);
  const [scoresList, setscoresList] = useState([]);

  // handle input change
  const handleInputChange = (newValue, index, currList, setFunction) => {
    // const { name, value } = e.target;
    let list = [...currList];
    list[index] = newValue;
    setFunction(list);
  };

  // handle click event of the Remove button
  const handleRemoveClick = (index, currList, setFunction) => {
    let list = [...currList];
    list.splice(index, 1);
    setFunction(list);
  };

  // handle click event of the Add button
  const handleAddClick = (currList, setFunction) => {
    setFunction([...currList, '']);
  };

  return (
    <div className="form-container">
      <Title />

      <h2>Answer Types</h2>
      {typeList.map((x, i) => (
        <div className="form-field">
          <Autocomplete
            input={x}
            setInput={val => handleInputChange(val, i, typeList, setTypeList)}
          />

          {typeList.length !== 1 && <button
          className="button submit"
          onClick={() => handleRemoveClick(i, typeList, setTypeList)}>Remove</button>}
          {typeList.length - 1 === i && <button onClick={() => handleAddClick(typeList, setTypeList)}>Add</button>}
        </div>
      ))}

      <h2>Answers</h2>
      {answerList.map((x, i) => (
        <div className="form-field">
          <Autocomplete
            input={x}
            setInput={val => handleInputChange(val, i, answerList, setAnswerList)}
          />

          {answerList.length !== 1 && <button
          className="button submit"
          onClick={() => handleRemoveClick(i, answerList, setAnswerList)}>Remove</button>}
          {answerList.length - 1 === i && <button onClick={() => handleAddClick(answerList, setAnswerList)}>Add</button>}
        </div>
      ))}
      <button className="button submit" type="submit" onClick={() => console.log(getScores())}>Submit</button>

    </div>
  );
}

export default App;
