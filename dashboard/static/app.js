const currentPowerElem = document.getElementById('current-power');
const ctx = document.getElementById('powerChart').getContext('2d');

let powerChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Power (W)',
            data: [],
            borderColor: 'rgb(75, 192, 192)',
            fill: false,
            tension: 0.1
        }]
    },
    options: {
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'minute'
                }
            },
            y: {
                beginAtZero: true
            }
        }
    }
});

function updateData() {
    fetch('/api/consumption/current')
        .then(res => res.json())
        .then(data => {
            currentPowerElem.textContent = data.power;
        });

    fetch('/api/consumption/history')
        .then(res => res.json())
        .then(history => {
            powerChart.data.labels = history.map(item => new Date(item.timestamp * 1000));
            powerChart.data.datasets[0].data = history.map(item => item.power);
            powerChart.update();
        });
}

setInterval(updateData, 5000);
updateData();
