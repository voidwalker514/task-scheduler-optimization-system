let profitChartInstance = null;
let statusChartInstance = null;

document.addEventListener('DOMContentLoaded', () => {
    const refreshBtn = document.getElementById('refresh-btn');
    
    refreshBtn.addEventListener('click', () => {
        refreshBtn.style.transform = 'scale(0.95)';
        setTimeout(() => refreshBtn.style.transform = '', 150);
        fetchData();
    });

    fetchData();
});

async function fetchData() {
    try {
        const response = await fetch('/api/schedule');
        const data = await response.json();
        renderDashboard(data);
    } catch (error) {
        console.error("Error fetching schedule data:", error);
    }
}

function renderDashboard(data) {
    // Animate numbers
    animateValue("total-profit", parseInt(document.getElementById("total-profit").innerText) || 0, data.total_profit, 1000);
    animateValue("time-spent", parseInt(document.getElementById("time-spent").innerText) || 0, data.total_time_spent, 1000, "h");
    
    const rate = Math.round((data.completed_count / data.total_tasks) * 100) || 0;
    animateValue("completion-rate", parseInt(document.getElementById("completion-rate").innerText) || 0, rate, 1000, "%");

    // Render Charts
    renderCharts(data);

    // Render Timeline
    const timelineContainer = document.getElementById('timeline-container');
    timelineContainer.innerHTML = '';
    
    data.completed_tasks.forEach((task, index) => {
        const item = document.createElement('div');
        item.className = 'task-item';
        item.style.animation = `fadeSlideUp 0.4s ease-out ${index * 0.1}s backwards`;
        
        item.innerHTML = `
            <div class="task-time">
                T:${task.start} ➝ T:${task.end}
            </div>
            <div class="task-details">
                <h4>${task.name}</h4>
                <div class="task-meta">
                    <span class="tag">Priority ${task.priority}</span>
                    <span>Duration: ${task.duration}h</span>
                </div>
            </div>
            <div class="task-profit">
                +${task.profit}
            </div>
        `;
        timelineContainer.appendChild(item);
    });

    // Render Missed
    const missedList = document.getElementById('missed-list');
    missedList.innerHTML = '';
    
    if (data.missed_tasks.length === 0) {
        missedList.innerHTML = `<p style="color: var(--text-muted); text-align: center; padding: 2rem 0;">No missed deadlines! 🎉</p>`;
    } else {
        data.missed_tasks.forEach((task, index) => {
            const item = document.createElement('div');
            item.className = 'missed-item';
            item.style.animation = `fadeSlideUp 0.4s ease-out ${index * 0.1}s backwards`;
            
            item.innerHTML = `
                <h4>${task.name}</h4>
                <div class="missed-meta">
                    <span>Deadline: T=${task.deadline}</span>
                    <span>Needed: ${task.duration}h</span>
                </div>
            `;
            missedList.appendChild(item);
        });
    }
}

// Number animation utility
function animateValue(id, start, end, duration, suffix = "") {
    if (start === end) return;
    const obj = document.getElementById(id);
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const current = Math.floor(progress * (end - start) + start);
        obj.innerHTML = current + (suffix ? `<span>${suffix}</span>` : "");
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

function renderCharts(data) {
    const profitCtx = document.getElementById('profitChart').getContext('2d');
    const statusCtx = document.getElementById('statusChart').getContext('2d');

    if (profitChartInstance) profitChartInstance.destroy();
    if (statusChartInstance) statusChartInstance.destroy();

    const taskNames = data.completed_tasks.map(t => t.name);
    const taskProfits = data.completed_tasks.map(t => t.profit);

    // Dynamic gradient for bars
    const gradient = profitCtx.createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, 'rgba(62, 99, 255, 0.8)');
    gradient.addColorStop(1, 'rgba(138, 63, 255, 0.2)');

    profitChartInstance = new Chart(profitCtx, {
        type: 'bar',
        data: {
            labels: taskNames,
            datasets: [{
                label: 'Profit Earned',
                data: taskProfits,
                backgroundColor: gradient,
                borderColor: 'rgba(62, 99, 255, 1)',
                borderWidth: 1,
                borderRadius: 6,
                barPercentage: 0.6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: { 
                    beginAtZero: true, 
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#8F95B2', font: { family: 'Outfit' } }
                },
                x: { 
                    grid: { display: false },
                    ticks: { color: '#8F95B2', font: { family: 'Outfit' } }
                }
            }
        }
    });

    statusChartInstance = new Chart(statusCtx, {
        type: 'doughnut',
        data: {
            labels: ['Completed', 'Missed'],
            datasets: [{
                data: [data.completed_count, data.missed_tasks.length],
                backgroundColor: [
                    'rgba(0, 240, 144, 0.8)',
                    'rgba(255, 59, 92, 0.8)'
                ],
                borderColor: [
                    'rgba(0, 240, 144, 1)',
                    'rgba(255, 59, 92, 1)'
                ],
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { 
                    position: 'bottom', 
                    labels: { color: '#FFFFFF', font: { family: 'Outfit' }, padding: 20 }
                }
            },
            cutout: '75%'
        }
    });
}
