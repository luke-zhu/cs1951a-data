var margin = {top: 100, right: 100, bottom: 100, left: 100},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var parseTime = d3.timeParse("%y-%m")
var formatTime = d3.timeFormat("%y-%m")

// set the ranges
var x = d3.scaleTime().range([0, width]);
x.ticks(d3.timeMonth.every(1));
var y = d3.scaleLinear().range([height, 0]);

// define the line
var valueline = d3.line()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[1]); });

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");
// Get the data
d3.json("data/posts-top.json", function(error, data) {
  if (error) throw error;
  // format the data
  
  var aggregated_data = {}

  data.forEach(function(d) {
    var date = formatTime(d3.isoParse(d.datetime))
    // console.log(d.title)
    if (aggregated_data[date]) {
      aggregated_data[date] += d.title.includes('') ? 1 : 0
    } else {
      aggregated_data[date] = d.title.includes('') ? 1 : 0
    }
  });

  var data_arr = Object.keys(aggregated_data)
    .map(key => [parseTime(key), aggregated_data[key]])
    .sort((a, b) => a[0] - b[0])

  console.log(data_arr)

  // Scale the range of the data
  x.domain(d3.extent(data_arr, function(d) { return d[0]; }));
  y.domain([0,
    //d3.max(data_arr, function(d) { return d[1]; })]);
    100]);
  // Add the valueline path.
  svg.append("path")
      .data([data_arr])
      .attr("class", "line")
      .attr("d", valueline);
  /*
  svg.append("path")
      .data([[[parseTime("12-10"), 1], [parseTime("17-04"), 40]]])
      .attr("class", "line2")
      .attr("d", valueline);
  */
  // Add the X Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));
  // Add the Y Axis
  svg.append("g")
      .call(d3.axisLeft(y));
});
