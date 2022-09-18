FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 5000
EXPOSE 5001
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

RUN rm -rf /app/*
RUN rm -rf /src/*

WORKDIR /src
COPY . .

RUN dotnet restore
RUN dotnet publish -c Release -o /app 

WORKDIR /
RUN rm -rf /src
WORKDIR /app


RUN dotnet dev-certs https
RUN dotnet dev-certs https --trust
ENTRYPOINT ["dotnet", "/app/grpcserv1.dll"]
