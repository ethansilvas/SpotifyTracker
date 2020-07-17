import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Login from "./components/Login.js";
import "bootstrap/dist/css/bootstrap.min.css";

class App extends Component {
    render() {
        return (
            <Router>
                <div className="container">
                    <nav className="navbar navbar-expand-lg navbar-light bg-light">
                        <Link to="/" className="navbar-brand">SpotifyTracker</Link>
                        <div className="collpase navbar-collapse">
                        <ul className="navbar-nav mr-auto">
                            <li className="navbar-item">
                            <Link to="/" className="nav-link">Login</Link>
                            </li>
                        </ul>
                        </div>
                    </nav>
                    <br />
                    
                    <Route path="/" exact component={Login} />
                </div>
            </Router>
        );
    }
}

export default App;
