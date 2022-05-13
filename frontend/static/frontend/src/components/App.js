import React, { Component } from "react";
import { render } from "react-dom";
import FormLogin from "./FormLogin.jsx";

export default class App extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		return <FormLogin />;
	}
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);