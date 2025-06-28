
import { CheckCircle, Shield, Zap, Users, Lock, Award } from "lucide-react";

const WhyChooseUs = () => {
  const benefits = [
    {
      icon: Award,
      title: "Insurance Industry Focus",
      description: "Specifically engineered for insurance professionals and fintech innovation"
    },
    {
      icon: Shield,
      title: "Regulatory Compliance",
      description: "Full adherence to BFSI regulations and health disclosure requirements"
    },
    {
      icon: Zap,
      title: "Advanced AI Technology",
      description: "Cutting-edge machine learning and real-time risk assessment capabilities"
    },
    {
      icon: Users,
      title: "Comprehensive Support",
      description: "Designed for insurers, brokers, agents, and modern fintech solutions"
    }
  ];

  return (
    <div className="bg-gradient-to-br from-emerald-50 via-teal-50 to-cyan-50 py-20">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-800 mb-6">
            ⚡ Why Choose Our Platform?
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Purpose-built for the insurance industry with state-of-the-art AI technology
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
          {benefits.map((benefit, index) => (
            <div key={index} className="group bg-white/70 backdrop-blur-lg p-8 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 border border-emerald-100/50">
              <div className="bg-gradient-to-br from-emerald-500 to-teal-600 w-16 h-16 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                <benefit.icon className="h-8 w-8 text-white" />
              </div>
              <h3 className="text-xl font-bold text-gray-800 mb-3">{benefit.title}</h3>
              <p className="text-gray-600 leading-relaxed">{benefit.description}</p>
            </div>
          ))}
        </div>

        <div className="bg-gradient-to-r from-emerald-500/10 to-cyan-500/10 backdrop-blur-lg rounded-3xl p-10 text-center border border-emerald-200/50 shadow-xl">
          <div className="flex items-center justify-center gap-3 mb-6">
            <Lock className="h-7 w-7 text-emerald-600" />
            <span className="text-2xl font-bold text-gray-800">🛡️ Security & Privacy First</span>
          </div>
          <p className="text-lg text-gray-700 leading-relaxed max-w-4xl mx-auto">
            <strong className="text-emerald-700">🎯 Begin your journey. Discover insights. Take decisive action.</strong><br />
            All sensitive data is processed with enterprise-grade security and complete confidentiality.
          </p>
        </div>
      </div>
    </div>
  );
};

export default WhyChooseUs;
