const renderChart=(data,labels)=>{
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Last 6 months Incomes',
                data: data,
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: true,
            legend: {
                display: true,
                position: 'bottom' 
            },
            title: {
                display: true,
                text: "Incomes per category",
            }
        }
    });

}

const getChartData=()=>{
    fetch("income_source_summary")
    .then((res)=>res.json())
    .then((results)=>{
        console.log("results",results);
        const source_data = results.income_source_data;
        const [labels, data]=[Object.keys(source_data),
            Object.values(source_data),
        ];
        renderChart(data,labels);
    })
}

window.onload = getChartData();
