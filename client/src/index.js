import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import PrivateRoute from "./components/PrivateRoute";
import HomeComponent from './views/Home';
import LoginComponent from './views/Login';
import DashboardComponent from "./views/Dashboard";
import UserConsentComponent from "./views/UserConsent";
import NotificationSetupComponent from "./views/NotificationSetup";

ReactDOM.render(
    <BrowserRouter>
        <Switch>
            <Route path="/login" component={LoginComponent}/>
            <Route path="/dashboard" component={DashboardComponent}/>
            <Route path="/user-consent" component={UserConsentComponent}/>
            <Route path="/notification-setup" component={NotificationSetupComponent}/>
            <PrivateRoute path="/private" component={HomeComponent}/>
        </Switch>
    </BrowserRouter>,
    document.getElementById('root')
);
