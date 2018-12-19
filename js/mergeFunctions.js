
const csv = require('csv-parser');
const fs = require('file-system')
const path = require('path');

const createCsvWriter = require('csv-writer').createObjectCsvWriter;

export const readMe = (hour, plusNum) => {

    var results = [];
    var hourPlus = parseInt(hour) + parseInt(plusNum);
    var hourly = parseInt(hour);

    var newFile = path.join(__dirname, hourly.toString(), "-", hourPlus.toString(), "/quotes.csv")
    var newDir = path.join(__dirname, hourly.toString(), "-", hourPlus.toString())

    fs.mkdir(newDir, () => {
        console.log('created dir for hour' + hour.toString())
    })

    // create csv write file
    fs.writeFile(newFile, "hi", (err) => {
        if (err) {
            return console.log(err);
        }
        console.log('created write file')
    })

    for (var i = hourly; i < hourPlus; i++) {


        var link = path.join(__dirname, 'files/', i.toString(), '/quotes.csv')
        console.log(link)
        fs.createReadStream(link)
            .pipe(csv())
            .on('data', (dat) => results.push(dat))
            .on('end', () => {



                // create csv column labels
                var csvWriter = createCsvWriter({
                    path: 'mergedFiles/' + hour.toString() + '/quotes.csv',
                    header: [
                        { id: 'timestamp', title: 'timestamp' },
                        { id: 'reformattedDate', title: 'reformattedDate' },
                        { id: 'hour', title: 'hour' },
                        { id: 'symbol', title: 'symbol' },
                        { id: 'bidPrice', title: 'bidPrice' },
                        { id: 'bidSize', title: 'bidSize' },
                        { id: 'askPrice', title: 'askPrice' },
                        { id: 'askSize', title: 'askSize' },
                        { id: 'midPrice', title: 'midPrice' },
                        { id: 'microPrice', title: 'microPrice' }
                    ]
                })

                //write records to csv file
                csvWriter.writeRecords(results)
                    .then(() => {
                        console.log('wrote records')
                    })
                    .catch((err) => console.log(err))



            })




    }

    return results;

}