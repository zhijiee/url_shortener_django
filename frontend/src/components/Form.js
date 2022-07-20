import React, { Component } from "react";
import ReactDOM from 'react-dom/client'

const axios = require('axios').default;
const APP_ID = 'app'

class UrlForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { url: '', response: null };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    // https://reactjs.org/docs/forms.html
    // For handling multiple input change, can refer to this
    handleChange(event) {
        this.setState({url: event.target.value});
    }

    // TODO: Currently using javascript.. Will convert to react render
    handleSubmit(event) {
        event.preventDefault();
        axios.post('/api/shorten/', {
            url: this.state.url
        }).then((response) => {
            document.getElementById(APP_ID).innerHTML = response.data;
            // this.state.response = response.data;
        // }).catch((error) => {
        }).catch(function (error) {
            console.log(error);
            // document.getElementById(APP_ID).innerHTML = error.response.data;
            alert(error.response.data)
            // this.state.response = error.response.data;
        });
    }


    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Enter a URL to shorten:<br />
                    <input type="text" name='url' value={this.state.url} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}

const root = ReactDOM.createRoot(
    document.getElementById('app')
);

root.render(<UrlForm />);