import React, { Component } from "react";
import ReactDOM from 'react-dom/client'

const axios = require('axios').default;
const APP_ID = 'app'

const root = ReactDOM.createRoot(
    document.getElementById('app')
);

class UrlForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { url: '', element: null };

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
            console.log(response.data.message);
            this.element = <div> URL: <a href={response.data.message}>{response.data.message}</a> </div>;
            root.render(this.element);
        }).catch(function (error) {
            console.log(error);
            const element = <div>Failed due to incorrect URL <br />Error:{error.message}</div>;
            root.render(element);
        })
        // .then(function () {
        // });
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

root.render(<UrlForm />);