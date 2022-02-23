import { useState } from 'react';
import Autosuggest from 'react-autosuggest';

const Autocomplete = () => {
  const [input, setInput] = useState('');
  const [suggestions, setSuggestions] = useState([]);

  const getSuggestions = async ({ value }) => {
    const apiUrl = 'https://www.wikidata.org/w/api.php?';
    let params = {
      action: 'wbsearchentities',
      search: value,
      language: 'en',
      format: 'json',
      origin: '*'
    };
    let searchParams = new URLSearchParams(params);

    const response = await fetch(apiUrl + searchParams.toString());
    const data = await response.json();
    setSuggestions(data.search ? data.search : []);
  };

  const getSuggestionValue = suggestion => suggestion.label + ' | ' + suggestion.id;

  const renderSuggestion = suggestion => (
    <span>
      {suggestion.label} | {suggestion.description} | {suggestion.id}
    </span>
  );

  return (
    <div>
      <h1>Test autocomplete</h1>
      <Autosuggest
        suggestions={suggestions}
        onSuggestionsFetchRequested={getSuggestions}
        onSuggestionsClearRequested={() => setSuggestions([])}
        getSuggestionValue={getSuggestionValue}
        renderSuggestion={renderSuggestion}
        inputProps={{value: input, onChange: (ev, { newValue }) => setInput(newValue), placeholder: 'Answer here'}}
      />
    </div>
  );
}

export default Autocomplete;
