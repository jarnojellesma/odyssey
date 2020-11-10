export function saveToken(token) {
    localStorage.setItem("token", token);
}

export function getToken() {
    return localStorage.getItem("token");
}

export function clearToken() {
    return localStorage.removeItem("token");
}

export function isAuthenticated() {
    return getToken() != null;
}

export default {
    saveToken,
    getToken,
    clearToken,
    isAuthenticated,
}
