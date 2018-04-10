len = 10000;

tic;
data = cell(len, 1);
sum_t = toc;
% data = zeros(len, 1);
times = {};
for n=1:len
    tic;
    data(n) = {0};
    % data(n) = 0;
    sum_t = sum_t + toc;

    if mod(n, len/100) == 0
        times(end+1) = {sum_t};
        sum_t = 0;
    end
end

times_prealloc = cell2mat(times);

tic;
data = {};
% data = [];
sum_t = toc;
times = {};
for n=1:len
    tic;
    data(end+1) = {0};
    % data(end+1) = 0;
    sum_t = sum_t + toc;

    if mod(n, len/100) == 0
        times(end+1) = {sum_t};
        sum_t = 0;
    end
end

times_end = cell2mat(times);

tic;
data = {};
% data = [];
sum_t = toc;
times = {};
for n=1:len
    tic;
    data = [data {0}];
    % data = [data 0];
    sum_t = sum_t + toc;

    if mod(n, len/100) == 0
        times(end+1) = {sum_t};
        sum_t = 0;
    end
end

times_append = cell2mat(times);

figure;
lines = semilogy(1:len/100:len, times_prealloc, 1:len/100:len, times_end, 1:len/100:len, times_append);
[lines.LineWidth] = deal(2);
legend(sprintf('prealloc (total: %.3f s)', sum(times_prealloc)), ...
       sprintf('end+1    (total: %.3f s)', sum(times_end)), ...
       sprintf('append   (total: %.3f s)', sum(times_append)));
ylabel('time to append in seconds');
xlabel('nth element');
print('array_performance', '-dpng', '-r300');
