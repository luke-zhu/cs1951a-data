let margin = {top: 100, right: 100, bottom: 100, left: 100};
let width = 960 - margin.left - margin.right;
let height = 500 - margin.top - margin.bottom;

let x = d3.scaleLinear().range([0, width]);
let y = d3.scaleLinear().range([height, 0]);

let svg = d3.select('#scatterplot')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform', `translate(${margin.left},${margin.top})`);

d3.json('data/scatterplot_data.json', (error, data) => {
  if (error) throw error;

  x.domain([40, 100]);
  y.domain([-0.5, 0.5]);

  svg.append('g')
    .attr('class', 'dots')
    .selectAll('dot')
    .data(data)
    .enter()
    .append('circle')
    .attr('class', 'dot')
    .attr('cx', d => x(d.avg_score))
    .attr('cy', d => y(d.sentiment))
    .attr('r', d => 3)
    .attr('title', d => d.artist)
    .attr('fill', 'steelblue');

  svg.append('g')
    .attr('class', 'dot-labels')
    .selectAll('text')
    .data(data.filter(d => d.num_albums >= 5))
    .enter()
    .append('text')
    .attr('transform', 'rotate(-45)')
    .attr('transform-origin', d => `${x(d.avg_score)} ${y(d.sentiment)}`)
    .attr('text-align', 'start')
    .attr('x', d => x(d.avg_score) + 4)
    .attr('y', d => y(d.sentiment) - 3)
    .text(d => d.artist)
    .attr('font-size', 8);

  svg.append('g')
    .attr('class', 'x axis')
    .attr('transform', `translate(0,${height / 2})`)
    .call(d3.axisBottom(x));
  svg.append('g')
    .attr('class', 'y axis')
    .call(d3.axisLeft(y));
})