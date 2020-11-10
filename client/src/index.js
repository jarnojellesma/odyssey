import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import PrivateRoute from "./util/PrivateRoute";
import Home from './views/Home';
import Login from './views/Login';

ReactDOM.render(
    <BrowserRouter>
        <Switch>
            <Route path="/login" component={Login}/>
            <PrivateRoute path="/" component={Home}/>
        </Switch>
    </BrowserRouter>,
    document.getElementById('root')
);
