import React from 'react';
import {makeStyles} from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import FormGroup from "@material-ui/core/FormGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import SaveIcon from "@material-ui/icons/Save";
import Layout from "../components/Layout";


const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(3),
        marginBottom: theme.spacing(3),
        padding: theme.spacing(2),
        [theme.breakpoints.up(600 + theme.spacing(3) * 2)]: {
            marginTop: theme.spacing(6),
            marginBottom: theme.spacing(6),
            padding: theme.spacing(3),
        },
    },
    header: {
        marginBottom: theme.spacing(3),
    },
    buttons: {
        display: 'flex',
        justifyContent: 'flex-end',
    },
    button: {
        marginTop: theme.spacing(3),
        marginLeft: theme.spacing(1),
    },
}));


export default function UserConsentComponent() {
    const classes = useStyles();

    const [state, setState] = React.useState({
        checkedA: true,
        checkedB: true,
        checkedF: true,
        checkedG: true,
    });

    const handleChange = (event) => {
        setState({...state, [event.target.name]: event.target.checked});
    };

    return (
        <Layout>
            <Paper className={classes.paper}>
                <React.Fragment>
                    <Typography component="h1" variant="h4" align="center" className={classes.header}>
                        User Consent
                    </Typography>
                </React.Fragment>
                <React.Fragment>
                    <FormGroup row>
                        <FormControlLabel
                            control={
                                <Checkbox
                                    checked={state.checkedB}
                                    onChange={handleChange}
                                    name="checkedB"
                                    color="primary"
                                />
                            }
                            label="Would you like to receive notifications to stimulate sustainable behavior?"
                        />
                    </FormGroup>
                    <FormGroup row>
                        <FormControlLabel
                            control={
                                <Checkbox
                                    checked={state.checkedB}
                                    onChange={handleChange}
                                    name="checkedB"
                                    color="primary"
                                />
                            }
                            label="Would you like to receive notifications about your energy usage?"
                        />
                    </FormGroup>
                    <FormGroup row>
                        <FormControlLabel
                            control={
                                <Checkbox
                                    checked={state.checkedB}
                                    onChange={handleChange}
                                    name="checkedB"
                                    color="primary"
                                />
                            }
                            label="Would you like to receive notifications in order to balance the grid?"
                        />
                    </FormGroup>

                </React.Fragment>

                <React.Fragment>
                    <div className={classes.buttons}>
                        <Button
                            variant="contained"
                            color="primary"
                            size="small"
                            className={classes.button}
                            startIcon={<SaveIcon/>}
                        >
                            Save
                        </Button>
                    </div>
                </React.Fragment>
            </Paper>
        </Layout>
    );
}