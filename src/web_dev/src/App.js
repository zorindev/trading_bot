import React from 'react';
import {HashRouter as Router, Switch, Route} from "react-router-dom";
import Home from "./pages/Home.js";
import Error from "./pages/Error.js";

const App = () => {

    return(
        <React.Fragment>

            <Router>

                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="*" component={Error} />

                </Switch>
            </Router>
        </React.Fragment>
    );
}

export default App;