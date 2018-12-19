
import { fetchHours, fetchTicks } from './fetch_functions';



// var hour = "18121403";
var hour = process.argv[2];
var symbol = process.argv[3];
var hours = process.argv[4];

var hoursPlus = parseInt(hour) + parseInt(hours)
console.log(hour, hoursPlus);

let fetchRicks = (hour, symbol) => {
    fetchHours(hour, symbol)
    fetchTicks(hour, symbol)
}


for (var i = parseInt(hour); i < hoursPlus; i++) {
    setTimeout(

        function () {
            fetchRicks(i.toString(), symbol)
        }, 10000);
}

