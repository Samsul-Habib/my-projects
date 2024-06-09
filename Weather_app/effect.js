// Function to fetch weather data from OpenWeatherMap API and update background image
function fetchWeather(city) {
    // Your fetchWeather function code goes here...
}

// Function to update background image based on weather description
function updateBackgroundBasedOnWeather(weatherDescription) {
    // Your updateBackgroundBasedOnWeather function code goes here...
}

// Function to handle button click event
document.getElementById('get-weather-btn').addEventListener('click', function() {
    const city = document.getElementById('city-input').value;
    fetchWeather(city);
});

// Function to update time and date
function updateTimeAndDate() {
    const now = new Date();
    //const timeElement = document.getElementById('time');
    //const dateElement = document.getElementById('date');

    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const formattedDate = now.toLocaleDateString('en-US', options);

    timeElement.textContent = now.toLocaleTimeString('en-US');
    dateElement.textContent = formattedDate;
}

// Update time and date every second
setInterval(updateTimeAndDate, 1000);
